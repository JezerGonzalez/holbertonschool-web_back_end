import Building from './5-building'

export default class SkyHighBuilding extends Building {
    constructor(sqft, floors){
        super(sqft);
        this.floors = floors;
        if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
            throw new Error('Class extending Building must override evacuationWarningMessage');
        }
    }

    get sqft(){
        return this.sqft;
    }

    get floors(){
        return this.floors;
    }
}