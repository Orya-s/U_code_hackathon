class MetaDataApi extends Api {
	constructor(resources = "", apiInterface = new AjaxCall()) {
		super(apiInterface, `http://localhost:8000/`)
		this.resources = resources
	}

	async getData(weather, location) {
		this.data = {
			"weather": weather,
			"location": location,
		}
		this.resources = "vacation"
		return await this.callApi()
	}

	async getWeatherOptions() {
		this.resources = "options/weather"
		return await this.callApi()
	}

	async getLocationOptions() {
		this.resources = "options/location"
		return await this.callApi()
	}

	//restful extention, not fully implemented
	async postData(data = "") {
		this.method = "POST"
		return await this.callApi(5, data)
	}

	//restful extention, not fully implemented
	async deleteData(data = "") {
		this.method = "DELETE"
		this.resources = data
		return await this.callApi(5, data)
	}
}
