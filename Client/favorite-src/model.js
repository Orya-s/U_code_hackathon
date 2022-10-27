const recipeModel = function () {
	let metaInstance
	let cacheData

	function getCache() {
		return cacheData
	}

	function initData() {
		metaInstance = new MetaDataApi()
	}

	async function getData(location, date) {
		let promise = metaInstance.getData(location, date)
		return await Promise.all([promise]).then(function (results) {
			cacheData = results[0]
			return results[0]
		})
	}

	return {
		getCache,
		getData,
		initData,
	}
}
