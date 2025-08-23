import taskBlock from './1-block-scoped.js';

describe('taskBlock function', () => {
  test('returns an array with false and true when argument is true', () => {
    expect(taskBlock(true)).toEqual([false, true]);
  });

  test('returns an array with false and true when argument is false', () => {
    expect(taskBlock(false)).toEqual([false, true]);
  });
});
