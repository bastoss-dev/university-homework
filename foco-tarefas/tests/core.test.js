'use strict';
const test=require('node:test');
const assert=require('node:assert/strict');
const {TaskManager,validateTask}=require('../js/core.js');
function make(){
 const data=new Map();let count=0;
 const storage={getItem:k=>data.has(k)?data.get(k):null,setItem:(k,v)=>data.set(k,String(v)),removeItem:k=>data.delete(k)};
 const manager=new TaskManager(storage,{id:()=>`id-${++count}`,now:()=>new Date(2026,10,9).toISOString()});
 return {manager,storage};
}
const sample=(title='Estudar Engenharia de Software',extra={})=>({title,description:'Revisar requisitos',category:'Estudos',priority:'Alta',status:'Pendente',dueDate:'2026-11-13',...extra});
test('CT01 - Cadastrar tarefa',()=>{const {manager:m}=make();const t=m.create(sample());assert.equal(m.list().length,1);assert.equal(m.get(t.id).title,sample().title)});
test('CT02 - Buscar por texto e filtrar',()=>{const {manager:m}=make();m.create(sample('Estudar UML'));m.create(sample('Comprar livro',{category:'Pessoal'}));assert.equal(m.filter({search:'uml'}).length,1);assert.equal(m.filter({category:'Pessoal'}).length,1)});
test('CT03 - Editar uma tarefa',()=>{const {manager:m}=make();const t=m.create(sample());m.update(t.id,{title:'Projeto revisado',priority:'Média'});assert.equal(m.get(t.id).priority,'Média');assert.equal(m.get(t.id).title,'Projeto revisado')});
test('CT04 - Alterar status e estatísticas',()=>{const {manager:m}=make();const a=m.create(sample());m.create(sample('Outra tarefa'));m.setStatus(a.id,'Concluída');assert.equal(m.stats().percent,50);assert.equal(m.stats().complete,1)});
test('CT05 - Excluir tarefa',()=>{const {manager:m}=make();const a=m.create(sample());assert.equal(m.remove(a.id),true);assert.equal(m.list().length,0)});
test('CT06 - Impedir cadastro sem título',()=>{const {manager:m}=make();assert.throws(()=>m.create(sample(' ')));assert.equal(m.list().length,0)});
test('CT07 - Exportar e importar JSON',()=>{const {manager:m}=make();m.create(sample());const backup=m.exportData();const {manager:n}=make();assert.equal(n.importData(backup),1);assert.equal(n.list().length,1)});
test('CT08 - Rejeitar backup inválido',()=>{const {manager:m}=make();assert.throws(()=>m.importData('{}'),/campo tasks/)});
test('CT09 - Rejeitar enumeração inválida',()=>{assert.throws(()=>validateTask(sample('Teste',{priority:'Urgentíssima'})),/inválida/)});
test('CT10 - Compartilhar persistência entre instâncias',()=>{const {manager:m,storage}=make();m.create(sample());const other=new TaskManager(storage);assert.equal(other.list().length,1)});
