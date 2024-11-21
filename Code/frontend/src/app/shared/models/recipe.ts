export class Recipe {

    public id : number;
    public user_id : number;
    public name : string;
    public description : string;
    public link : string;


    constructor(id : number, user_id : number, name:string, description:string, link:string){
        this.id = id;
        this.user_id=user_id;
        this.name=name;
        this.description=description;
        this.link=link;
    }

}
