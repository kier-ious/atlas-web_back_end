export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    fakeTimer(() => {
      let success = true;
      if (success) {
        resolve( 'API Respose Data');
      } else {
        reject(new TypeError('Failed to fetch data'));
      }
    }, 3000);
  });
}
