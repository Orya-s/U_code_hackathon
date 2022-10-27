const model = recipeModel()
const renderer = recipeRender()

Handlebars.registerHelper("chooseClass", (isDT) => (isDT ? "dt-item" : "item"))
Handlebars.registerHelper("dreamOptions", (isDT) =>
	isDT ? "Remove from top picks" : "Add to top picks"
)

const generateData = function (attempts, location, date) {
	model.initData()
	model
		.getData(location, date)
		.then((res) => {
			console.log(res)
			renderer.renderResults(res)
		})
		.catch((error) => errorHandeling(error, attempts, generateData))
}

$("#results").on("click", ".dreamteam-card-button", function () {
	let isDreamTeam = $(this).parent("div").attr("data-dt")
	let player_id = $(this).parent("div").attr("data-id")
	let player_data = model.getCache().find((p) => p.id == player_id)
	model.initDreamTeam()

	if (String(isDreamTeam).toLowerCase() == "true") {
		model
			.deletePlayer(player_id)
			.then((res) => renderer.renderCard(player_id, res.metaData))
	} else {
		model
			.addPlayer(player_data)
			.then((res) => renderer.renderCard(player_id, res.metaData))
	}
})

let errorHandeling = function (error, attempts, callback) {
	console.warn(error)
	if (attempts-- > 0) {
		console.warn(`coudlnt load user.\n
			Attampts left: ${attempts}\n
			trying again...`)
		callback(attempts)
	} else {
		console.log(`attampet limit reached, please check whats wrong`)
	}
}

generateData(5, "London", "2022/12/12")
