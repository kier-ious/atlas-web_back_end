import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return new Promise((resolve) => {
    Promise.allSettled([
      signUpUser(firstName, lastName),
      uploadPhoto(fileName),
    ])
      .then((results) =>
        resolve(
          results.map((result) => ({
            status: result.status,
            value: result.status === 'fulfilled' ? result.value : result.reason,
          }))
        )
      );
  });
}
