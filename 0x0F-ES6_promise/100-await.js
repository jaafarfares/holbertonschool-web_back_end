import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const first = await uploadPhoto();
    const second = await createUser();
    return { photo: first, user: escond };
  } catch (error) {
    return { photo: null, user: null };
  }
}
