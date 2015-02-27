text = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716"""

_ = require 'lodash'

keylog = (parseInt(el) for el in entry for entry in text.split('\n'))

# Permute by Oriol (http://stackoverflow.com/a/11509565)
`function permute(input) {
    var permArr = [],
    usedChars = [];
    function main(){
        var i, ch;
        for (i = 0; i < input.length; i++) {
            ch = input.splice(i, 1)[0];
            usedChars.push(ch);
            if (input.length == 0) {
                permArr.push(usedChars.slice());
            }
            main();
            input.splice(i, 0, ch);
            usedChars.pop();
        }
        return permArr;
    }
    return main();
}`

isOrdered = (trial) ->
  (entry) ->
    indicees = _.map(entry, (dig) -> _.indexOf(trial, dig))
    _.isEqual(indicees, _.sortBy(indicees))

digits = (arrayOfArrays) -> _(arrayOfArrays).flatten().uniq().value()

code = _(permute(digits(keylog)))
  .filter((trial) -> _.all(keylog, isOrdered(trial)))
  .first()
  .join('')

console.log(code) #=> 73162890