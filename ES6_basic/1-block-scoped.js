export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    (function() {
      let task = true;
      let task2 = false;
    })();
  }

  return [task, task2];
}
