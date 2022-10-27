const model = recipeModel()
const renderer = recipeRender()

Handlebars.registerHelper("dreamOptions", (isDT) =>
	isDT ? "Remove from Dream Team" : "Add to Dream Team"
)

const generateData = function (attempts, location, date) {
	model.initData()
	model
		.getData(location, date)
		.then((res) => renderer.renderResults(res))
		.catch((error) => errorHandeling(error, attempts, generateData))
}

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
