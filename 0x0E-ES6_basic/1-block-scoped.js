export default function taskBlock(trueOrFalse) {
  const task = false;
  onst task2 = true;

  if (trueOrFalse) {
    /* eslint-disable */
    const task = true;
    /* eslint-disable */
    const task2 = false;
  }

  return [task, task2];
}
