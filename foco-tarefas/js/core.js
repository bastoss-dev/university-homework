
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  if (root) root.FocoCore = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const STORAGE_KEY = 'foco-tarefas-v1';
  const CATEGORIES = ['Estudos', 'Trabalho', 'Pessoal'];
  const PRIORITIES = ['Baixa', 'Média', 'Alta'];
  const STATUSES = ['Pendente', 'Em andamento', 'Concluída'];

  function validateTask(data) {
    const title = String(data.title || '').trim();
    if (!title || title.length > 80) throw new Error('Informe um título de até 80 caracteres.');
    const description = String(data.description || '').trim();
    if (description.length > 400) throw new Error('A descrição pode ter no máximo 400 caracteres.');
    const category = String(data.category || 'Pessoal');
    const priority = String(data.priority || 'Média');
    const status = String(data.status || 'Pendente');
    const dueDate = String(data.dueDate || '');
    if (!CATEGORIES.includes(category)) throw new Error('Categoria inválida.');
    if (!PRIORITIES.includes(priority)) throw new Error('Prioridade inválida.');
    if (!STATUSES.includes(status)) throw new Error('Status inválido.');
    if (dueDate && (!/^\d{4}-\d{2}-\d{2}$/.test(dueDate) || Number.isNaN(Date.parse(dueDate + 'T12:00:00')))) {
      throw new Error('Data inválida.');
    }
    return { title, description, category, priority, status, dueDate };
  }

  function normalizeRecord(record) {
    if (!record || typeof record !== 'object' || typeof record.id !== 'string' || !record.id.trim()) {
      throw new Error('Registro de tarefa inválido.');
    }
    const safe = validateTask(record);
    const createdAt = typeof record.createdAt === 'string' && !Number.isNaN(Date.parse(record.createdAt))
      ? record.createdAt : new Date().toISOString();
    const updatedAt = typeof record.updatedAt === 'string' && !Number.isNaN(Date.parse(record.updatedAt))
      ? record.updatedAt : createdAt;
    return { id: record.id, ...safe, createdAt, updatedAt };
  }

  function makeId() {
    if (typeof crypto !== 'undefined' && crypto.randomUUID) return crypto.randomUUID();
    return 'task-' + Date.now() + '-' + Math.random().toString(36).slice(2, 10);
  }

  class TaskManager {
    constructor(storage, options = {}) {
      this.storage = storage;
      this.key = options.key || STORAGE_KEY;
      this.now = options.now || (() => new Date().toISOString());
      this.id = options.id || makeId;
    }
    list() {
      try {
        const raw = this.storage.getItem(this.key);
        if (!raw) return [];
        const values = JSON.parse(raw);
        if (!Array.isArray(values)) return [];
        return values.map(normalizeRecord).sort((a, b) => b.createdAt.localeCompare(a.createdAt));
      } catch (_) {
        return [];
      }
    }
    _save(records) { this.storage.setItem(this.key, JSON.stringify(records)); }
    get(id) { return this.list().find(task => task.id === id) || null; }
    create(data) {
      const safe = validateTask(data);
      const now = this.now();
      const item = { id: this.id(), ...safe, createdAt: now, updatedAt: now };
      this._save([item, ...this.list()]);
      return item;
    }
    update(id, changes) {
      const tasks = this.list();
      const i = tasks.findIndex(task => task.id === id);
      if (i < 0) throw new Error('Tarefa não encontrada.');
      const safe = validateTask({ ...tasks[i], ...changes });
      tasks[i] = { ...tasks[i], ...safe, updatedAt: this.now() };
      this._save(tasks);
      return tasks[i];
    }
    remove(id) {
      const tasks = this.list();
      const next = tasks.filter(task => task.id !== id);
      if (tasks.length === next.length) return false;
      this._save(next);
      return true;
    }
    setStatus(id, status) { return this.update(id, { status }); }
    filter({ search = '', status = 'Todas', category = 'Todas' } = {}) {
      const term = String(search).trim().toLocaleLowerCase('pt-BR');
      return this.list().filter(task =>
        (status === 'Todas' || task.status === status) &&
        (category === 'Todas' || task.category === category) &&
        (!term || [task.title, task.description].some(field => field.toLocaleLowerCase('pt-BR').includes(term)))
      );
    }
    stats() {
      const tasks = this.list();
      const total = tasks.length;
      const complete = tasks.filter(task => task.status === 'Concluída').length;
      return { total, complete, pending: tasks.filter(task => task.status === 'Pendente').length,
        inProgress: tasks.filter(task => task.status === 'Em andamento').length,
        percent: total ? Math.round(100 * complete / total) : 0 };
    }
    exportData() { return JSON.stringify({ application: 'Foco Tarefas', version: 1, tasks: this.list() }, null, 2); }
    importData(json) {
      const parsed = typeof json === 'string' ? JSON.parse(json) : json;
      if (!parsed || !Array.isArray(parsed.tasks)) throw new Error('Arquivo incompatível: campo tasks ausente.');
      if (parsed.tasks.length > 1000) throw new Error('Limite de 1000 tarefas por importação.');
      const records = parsed.tasks.map(normalizeRecord);
      if (new Set(records.map(item => item.id)).size !== records.length) throw new Error('IDs repetidos no arquivo.');
      this._save(records);
      return records.length;
    }
  }

  return { TaskManager, STORAGE_KEY, CATEGORIES, PRIORITIES, STATUSES, validateTask, normalizeRecord };
});

