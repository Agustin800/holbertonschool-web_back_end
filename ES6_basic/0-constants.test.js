import { taskFirst, taskNext } from './0-constants.js';

test('taskFirst uses const', () => {
  expect(taskFirst()).toBe('I prefer const when I can.');
});

test('taskNext uses let and concatenates getLast', () => {
  expect(taskNext()).toBe('But sometimes let is okay');
});
