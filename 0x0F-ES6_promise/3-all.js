import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      const photo = results[0].body;
      const { first, last } = results[1];
      console.log(`${photo} ${first} ${last}`);
    })
    .catch(() => console.log('Signup system offline'));
}
