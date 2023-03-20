import { uploadPhoto, createUser } from './utils.js';


async function asyncUploadUser() {
  try {
    return { photo: await uploadPhoto(), user: await createUser() };
  }
  catch (error) { return `photo: null, user: null`}
}

export default asyncUploadUser;
