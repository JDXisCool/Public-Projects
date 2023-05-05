function Home() {
    /* Properties */
    this.quoteControl =
        {
            quoteItems: null,
            currentItem: 0,
            numberOfItems: 0,
            interval: null,
            repeatPeriod: 5000
        };
 /* Methods */
this.initialiseQuoteControl = function () {

        /* Get all items in quote bar */
        let quoteItems = $(".quoteItem");

        /* Set values */
        this.quoteControl.quoteItems = quoteItems;
        this.quoteControl.numberOfItems = quoteItems.length;

        /* Initiate quote loop to show next item */
        let self = this;
        this.quoteControl.interval = setInterval(function () {
            self.showNextQuoteItem(self);
        }, this.quoteControl.repeatPeriod);
}
this.showNextQuoteItem = function (self) {
        /* fade out the current item */
        $(self.quoteControl.quoteItems).eq(self.quoteControl.currentItem).fadeOut('slow', function () {
            /* Increment current quote item counter*/
            if (self.quoteControl.currentItem >= (self.quoteControl.numberOfItems - 1)) {
                /* Reset counter to zero */
                self.quoteControl.currentItem = 0;
            } else {
                /* Increase counter by 1 */
                self.quoteControl.currentItem++;
            }
            /* fade in the next item*/
            $(self.quoteControl.quoteItems).eq(self.quoteControl.currentItem).fadeIn('slow');
        });
}
}
$(document).ready(function () {
    /* Instantiate new Home class */
    app.home = new Home();
 /* Initialize the Quote bar */
    app.home.initialiseQuoteControl();
});
