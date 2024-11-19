import { Component, OnInit } from "@angular/core";
import { UserService } from "../../shared/services/user.service"; 

@Component({
  selector: "app-login",
  templateUrl: "./login.component.html",
  styleUrls: ["./login.component.css"]
})

export class LoginComponent implements OnInit {
  userData;
  constructor(private user: UserService) {}

  ngOnInit() {
    this.user.currentUserData.subscribe(userData => (this.userData = userData));
  }

  changeData(event : any) {
    var msg = event.target.value;
    this.user.changeData(msg);
  }
  login(data : any) {
    this.user.changeData(data);
  }
}
