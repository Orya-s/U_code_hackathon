class MetaDataApi extends Api {
	constructor(resources = "", apiInterface = new AjaxCall()) {
		super(apiInterface, `http://localhost:8000/`)
		this.resources = resources
	}

	async getData(location, date) {
		this.data = {
			"location": location,
			"date": date,
		}
		this.resources = "hotels"
		return await this.callApi()
	}
}
