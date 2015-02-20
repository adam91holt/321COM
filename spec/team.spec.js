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
        it("should visit the site and see the login form", function(done) {
            browser.visit(url).then(function(done) {
                browser.assert.element('#teamCon');
                browser.assert.text('title', 'Football Mashup');
            }).then(function(done) {
                browser.assert.text('title', 'random', 'Wrong title');
            }).then(done, done)
        });
    })
});
// describe("Test Javascript", function() {
//     it("should have defined headless browser", function(next) {
//         expect(typeof browser != "undefined").toBe(true);
//         expect(browser instanceof Browser).toBe(true);
//         next();
//     });
//     it("should visit the site and see the teams", function(next) {
//         browser.visit(url, function(e, browser) {
//             assert.ok(browser.success);
//             if(browser.error) {
//                 console.dir("Errors reported:", browser.errors)
//             };
//         });
//         next();
//     });
//      it("it should be able to press a team", function(next) {
//         browser.visit(url, function(e, browser) {
//             assert.ok(browser.success);
//             if(browser.error) {
//                 console.dir("Errors reported:", browser.errors)
//             };
//         });
//         next();
//     });
//     .pressButton('input[value="Login"]', function() {
//             expect(browser.html("body")).not.toContain("Insanely fast, headless full-stack testing using Node.js");
//             expect(browser.query("input[value='Login']")).toBeDefined();
//             next();
//         });
//});
//
//
//function(err) {
//             expect(browser.success).toBe(true);
//             expect(browser.query("input[value='test']")).toBeDefined(); 
//         }