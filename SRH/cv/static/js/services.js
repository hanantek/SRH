'use strict';

app.factory('User', function($rootScope) {
	return {
		isAuthenticated: false,
		username: '',
		id: 0
	};
});