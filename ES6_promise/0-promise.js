export default function getResponseFromAPI(fakeTimer) {
  return new Promise((resolve, reject) => {
    fakeTimer(() => {
      const success = true;
      if (success) {
        resolve('API Respose Data');
      } else {
        reject(new TypeError('Failed to fetch data'));
      }
    }, 3000);
  });
}
