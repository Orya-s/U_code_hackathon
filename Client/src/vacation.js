const vacation = function () {
	let metaInstance
	let cacheData

	function getCache() {
		return cacheData
	}

	function initData() {
		metaInstance = new MetaDataApi()
	}

	async function fetchVacation(weather, location) {
		let promise = metaInstance.getData(weather, location)
		return await Promise.all([promise]).then(function (results) {
			cacheData = results[0]
			return results[0]
		})
	}

	//restful extention, not fully implemented
	async function addData(userInput) {
		let addedPlayerPromise = metaInstance.postData(userInput)
		return await Promise.all([addedPlayerPromise]).then(function (results) {
			return results[0]
		})
	}

	//restful extention, not fully implemented
	async function deleteData(userInput) {
		let addedPlayerPromise = metaInstance.deleteData(userInput)
		return await Promise.all([addedPlayerPromise]).then(function (results) {
			return results[0]
		})
	}

	return {
		getCache,
		fetchVacation,
		initData,
		addData,
		deleteData,
	}
}
