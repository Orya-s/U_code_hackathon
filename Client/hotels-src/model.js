const recipeModel = function () {
	let metaInstance
	let cacheData
	let dreamTeamInstance

	function getCache() {
		return cacheData
	}

	function initData() {
		metaInstance = new MetaDataApi()
	}

	function initDreamTeam() {
		dreamTeamInstance = new DreamTeamApi()
	}

	async function getData(location, date) {
		let promise = metaInstance.getData(location, date)
		return await Promise.all([promise]).then(function (results) {
			cacheData = results[0]
			return results[0]
		})
	}

	async function addPlayer(playerData) {
		let addedPlayerPromise = dreamTeamInstance.postData(playerData)
		return await Promise.all([addedPlayerPromise]).then(function (results) {
			return { metaData: results[0] }
		})
	}

	async function deletePlayer(playerId) {
		let addedPlayerPromise = dreamTeamInstance.deleteData(playerId)
		return await Promise.all([addedPlayerPromise]).then(function (results) {
			return { metaData: results[0] }
		})
	}

	return {
		getCache,
		getData,
		initData,
		initDreamTeam,
		addPlayer,
		deletePlayer,
	}
}
