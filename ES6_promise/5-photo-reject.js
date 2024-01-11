export default function uploadPhoto(filename) {
  return Promise.reject(new TypeError(`${filename}` + 'cannot be processed'));
}
