import axios from "axios";

// Asynchronously load country demographic data from Django backend
const loadGeometriesTask = async () => {
  try {
    const target = "http://localhost:8000/api/country/geometry/";
    console.debug(`Backend ${target}`);
    const response = await axios.get(target, {});
    return response.data.features;
  } catch (error) {
    console.log(error);
    return [];
  }
};

export default loadGeometriesTask;
