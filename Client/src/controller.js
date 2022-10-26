const model = vacation()
const renderer = view()

const generateData = function (attempts, weather, location) {
	model
		.fetchVacation(weather, location)
		.then((res) => renderer.renderResults(res))
		.catch((error) => errorHandeling(error, attempts, generateData))
}

$("body").bind("keypress", function (event) {
	if (event.keyCode === 13) {
		// let weather = $("#weather-input").val()
		// let location = $("#location-input").val()
		let weather = "hot"
		let location = "London"
		if (weather != "" && location != "") {
			model.initData()
			generateData(5, weather, location)
		} else console.warn("no input")
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
