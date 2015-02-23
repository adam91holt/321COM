var Browser = require("zombie");
var url = "http://mashup321com.appspot.com/";
var browser = new Browser();
jasmine.getEnv().defaultTimeoutInterval = 999999
describe("Homepage : ", function() {
    describe('browser : ', function() {
        it("should have defined headless browser", function(next) {
            expect(typeof browser != "undefined").toBe(true);
            expect(browser instanceof Browser).toBe(true);
            next();
        });
    })
    describe('checking the page', function() {
        it("The page should show the title", function(done) {
            browser.visit(url).then(function(done) {
                browser.assert.element('#teamCon');
                browser.assert.text('title', 'Football Mashup', 'wrong page title');
            }).then(function(done) {
                return browser.clickLink('#details_Chelsea')
            }).then(
        null,
        function(e) {
            console.log("An error occurred deep within func", e, "continuing");
        }
    ).then(function(done) {
                browser.assert.success()
                browser.assert.text('title', 'Chelsea', 'wrong page title');

            }).then(function(done) {
                //testing each element is on the page including the correct amount of elements
                browser.assert.element('#container');
                browser.assert.elements('.Tweet', 10);
                browser.assert.elements('.player', 28);
                browser.assert.element('#wikiHold');

            }).then(done, done)
        });
    })
});





