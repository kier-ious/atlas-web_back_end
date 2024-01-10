import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];

  Promise.all(promises)
    .then(() => {
      results.forEach(({ body, firstName, lastName }) => {
        console.log(`${body} ${firstName} ${lastName}`);
      });
    })
    .catch(() => {
      console.error('Signup system offline');
    });
}
