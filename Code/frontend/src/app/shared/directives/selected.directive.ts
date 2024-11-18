// selected-pizza.directive.ts

import { Directive, ElementRef, Input, Renderer2, HostBinding } from '@angular/core';

@Directive({
  selector: '[appSelectedPizza]'
})
export class SelectedDirective {
  @Input() set appSelectedPizza(value: boolean) {
    this.isSelected = value;
  }

  @HostBinding('style.backgroundColor') backgroundColor: string="";
  @HostBinding('style.color') textColor: string="";

  private isSelected: boolean=false;

  constructor(private el: ElementRef, private renderer: Renderer2) { }

  ngOnChanges() {
    if (this.isSelected) this.backgroundColor = 'blue';
      else this.backgroundColor = 'transparent';
    if (this.isSelected) this.textColor = 'white';
      else this.textColor = 'black';
  }
}
