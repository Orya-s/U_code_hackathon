const model = vacation()
const renderer = view()

const generateData = function (attempts, weather, location) {
	model
		.fetchVacation(weather, location)
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

$("body").bind("keypress", function (event) {
	if (event.keyCode === 13) {
		let weather = $("#weather-input").val()
		let location = $("#location-input").val()
		if (weather != "" && location != "") {
			model.initData()
			generateData(5, weather, location)
		} else console.warn("no input")
	}
})

$("#weather-input").on("click", function () {
	model.initData()
	model
		.fetchScrollbarOptions()
		.then((res) => renderer.appendScrollOptions(res))
		.catch((error) => errorHandeling(error, 5, () => {}))
})

$("#location-input").on("click", function () {
	model.initData()
	model
		.fetchLocationOptions()
		.then((res) => renderer.appendLoactionOptions(res))
		.catch((error) => errorHandeling(error, 5, () => {}))
})
