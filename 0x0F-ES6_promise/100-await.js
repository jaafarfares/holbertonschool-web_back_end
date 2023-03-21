import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    let first_response = await uploadPhoto('profile-photo');
    let second_response = await createUser()
    return { photo: first_response, user: second_response };
  } catch (error) {
    console.error(error);
    return { photo: null, user: null };
  }
}
