export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({ success: 200, body: 'Success' });
    } else {
      reject(new TypeError('The fake API is not working currently'));
    }
  });
}
