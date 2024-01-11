import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const photoUploadPromise = uploadPhoto(fileName);

  const results = await Promise.allSettled([signUpPromise, photoUploadPromise]);

  return results.map((result) => ({
    status: result.status,
    value: result.value || result.reason,
  }));
}
