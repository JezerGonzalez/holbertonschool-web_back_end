export default function getFullResponseFromAPI(success) {
  return new Promise((resolve) => {
    if (success === true) {
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
      throw Error({
        status: 500,
        body: 'The fake API is not working currently',
      });
    }
  });
}
