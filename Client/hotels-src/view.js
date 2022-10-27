const recipeRender = function () {
	const renderComponent = function (hbTemplate, elementToRender, metaData) {
		const source = $(hbTemplate).html()
		const template = Handlebars.compile(source)
		let newHTML = template(metaData)
		$(elementToRender).empty()
		$(elementToRender).append(newHTML)
	}
	const renderResults = function (res) {
		console.log(res)
		renderComponent("#results-template", "#results", res)
		appandImgs(res)
	}
	const appandImgs = function (results) {
		for (item of results.response) {
			let elementToRender = `#${item.id}`
			renderComponent("#imgs-template", elementToRender, item)
		}
	}

	return {
		renderResults,
		renderComponent,
		appandImgs,
	}
}
