const view = function () {
	const renderComponent = function (hbTemplate, elementToRender, metaData) {
		const source = $(hbTemplate).html()
		const template = Handlebars.compile(source)
		let newHTML = template(metaData)
		$(elementToRender).empty()
		$(elementToRender).append(newHTML)
	}

	const renderResults = function (res) {
		renderComponent("#results-template", "#results", res.response)
	}

	const appendScrollOptions = function (options) {
		renderComponent("#scroll-template", "#scroll-weather", options.response)
	}

	const appendLoactionOptions = function (options) {
		renderComponent(
			"#location-template",
			"#scroll-location",
			options.response
		)
	}

	return {
		renderResults,
		renderComponent,
		appendScrollOptions,
		appendLoactionOptions,
	}
}
