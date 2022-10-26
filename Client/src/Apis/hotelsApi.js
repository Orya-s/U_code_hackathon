// const settings = {
// 	"async": true,
// 	"crossDomain": true,
// 	"url": "https://hotels-com-provider.p.rapidapi.com/v1/hotels/search?checkin_date=2022-03-26&checkout_date=2022-03-27&sort_order=STAR_RATING_HIGHEST_FIRST&destination_id=1708350&adults_number=1&locale=en_US&currency=USD&star_rating_ids=5&page_number=1&guest_rating_min=4",
// 	"method": "GET",
// 	"headers": {
// 		"X-RapidAPI-Key": "f2c008de89msh4d900f07448d1f2p188b0djsnf040cbb7f293",
// 		"X-RapidAPI-Host": "hotels-com-provider.p.rapidapi.com"
// 	}
// };

// $.ajax(settings).done(function (response) {
// 	console.log(response);
// });

const settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://hotels-com-provider.p.rapidapi.com/v1/hotels/search?checkin_date=2022-03-26&checkout_date=2022-03-27&sort_order=STAR_RATING_HIGHEST_FIRST&destination_id=1708350&adults_number=1&locale=en_US&currency=USD&star_rating_ids=5&page_number=1&guest_rating_min=4",
	"method": "GET",
	"headers": {
		"X-RapidAPI-Key": "f2c008de89msh4d900f07448d1f2p188b0djsnf040cbb7f293",
		"X-RapidAPI-Host": "hotels-com-provider.p.rapidapi.com"
	}
};

$.ajax(settings).done(function (response) {
	console.log(response);
});