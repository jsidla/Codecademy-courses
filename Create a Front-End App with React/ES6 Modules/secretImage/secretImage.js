import { toggleHiddenElement, changeToFunkyColor } from "../modules/domFunctions.js";

const buttonElement = document.getElementById('secret-button');
const imgElement = document.getElementById('secret-img');

buttonElement.addEventListener('click', () => {
  toggleHiddenElement(imgElement);
  changeToFunkyColor(buttonElement);
});