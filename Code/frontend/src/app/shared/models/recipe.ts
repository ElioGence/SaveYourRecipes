export class Recipe {

    public id : number;
    public name : string;
    public description : string;
    public link : string;


    constructor(id:number, name:string, description:string, link:string){
        this.id=id;
        this.name=name;
        this.description=description;
        this.link=link;
    }

}

/**
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    instructions TEXT NOT NULL,
    link TEXT
);
 */