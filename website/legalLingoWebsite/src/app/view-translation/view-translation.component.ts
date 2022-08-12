import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup} from '@angular/forms';
import { Validators } from '@angular/forms';

@Component({
  selector: 'app-view-translation',
  templateUrl: './view-translation.component.html',
  styleUrls: ['./view-translation.component.css']
})
export class ViewTranslationComponent implements OnInit {

  constructor() { 
    this.spaceFormGroup.patchValue({
      termControl  :  "penalties",
      defControl : "Una penalisazion es un castigo para una persona que ha violado la ley, un contracto, una regla, o una regulation. Una penalisazion puede ser una respuesta a una violation criminal o civil, aunque penalisaziones civiles normalmente son menos severas."
    });

  }
  spaceFormGroup = new FormGroup({
    termControl : new FormControl('', [Validators.required, Validators.minLength(1)]), //space ID 
    defControl : new FormControl('', [Validators.required, Validators.minLength(1)]), //space ID 
  });

  nextTerm(){
    this.spaceFormGroup.patchValue({
      termControl  :  "requirements",
      defControl : "Una cualidad o cualificación que debes tener para ser permitido hacer algo o ser competente para algo."
    });

  }

  ngOnInit(): void {
  }

}
