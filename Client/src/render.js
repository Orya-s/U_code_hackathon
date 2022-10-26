
const pageRender = function () {

	const renderComponent = function (hbTemplate, elementToRender, metaData) {
		const source = $(hbTemplate).html()
		const template = Handlebars.compile(source)
		let newHTML = template(metaData)
		$(elementToRender).empty()
		$(elementToRender).append(newHTML)
	}

	const renderResults = function (res) {
		renderComponent("#results-template", "#results", res)
	}

	const appendScrollOptions = function (options) {
		renderComponent("#scroll-template", "#scroll-weather", options["weather"])
		renderComponent("#scroll-template", "#scroll-location", options["location"])
	}

	return {
		renderResults,
		renderComponent,
		appendScrollOptions,
	}
}
