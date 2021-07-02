import axios from "axios";

// Asynchronously load real restriction dates from Django backend
const loadRealDatesTask = async (iso_code) => {
  try {
    const target = `http://localhost:3000/api/country/importantdates/?iso_code=${iso_code}`;
    console.debug(`Backend ${target}`);
    const response = await axios.get(target, {});
    return response.data[0];
  } catch (error) {
    console.log(error);
    return [];
  }
};

export default loadRealDatesTask;
