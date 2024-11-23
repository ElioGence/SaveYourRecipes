import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  
  isSidebarOpen = false;

  openSideBar(): void {
    this.isSidebarOpen = true;
  }

  closeSideBar(): void {
    this.isSidebarOpen = false;
  }
}
