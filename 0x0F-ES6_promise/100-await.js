import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const first_response = await uploadPhoto('profile-photo');
    const second_response = await createUser()
    return { photo: first_response, user: second_response };
  } catch (error) {
    console.error(error);
    return { photo: null, user: null };
  }
}
