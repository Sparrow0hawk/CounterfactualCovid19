import axios from "axios";

class LoadGeometriesTask {
  retrieve = async () => {
    console.log("Loading geometries from Django backend...");
    try {
      const target = "http://localhost:8000/api/country/geometry/"
      console.log(`Getting ${target}`);
      const res = await axios.get(target, {});
      return res.data.features;
    } catch (error) {
      console.log(error);
      return [];
    }
  };
}

export default LoadGeometriesTask;
