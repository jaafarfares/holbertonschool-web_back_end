import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {    
    return { photo: await uploadPhoto('profile-photo'), user: await createUser() };
  } catch (error) {
    console.error(error);
    return { photo: null, user: null };
  }
}
