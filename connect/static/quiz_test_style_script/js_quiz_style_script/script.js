 document.addEventListener("DOMContentLoaded",()=>{
 const start_btn=document.querySelector('.start');
 const popup=document.querySelector('.pop_up');
 const main=document.querySelector('.main');
 const exitbtn=document.querySelector('.exitbtn');
 const continuebtn=document.querySelector('.continue');
 const quiz_sec=document.querySelector('.quiz_section');
 const quizBox=document.querySelector('.quiz-box');
 let nxtBtn=document.querySelector('.next-btn');
 let questionText=document.querySelector('.question-text');
 const optionList=document.querySelector('.optionlist');
 const resultBox=document.querySelector('.result-box');
 const restulScore=document.querySelector('.score-text');
 const tryAgainbtn=document.querySelector('.tryagain');
  const gohome=document.querySelector('.go-home');



 start_btn.onclick= () =>{
     console.log("start_btn has clicked");
 	popup.classList.add('active');
 	console.log("popup clicked");
 	main.classList.add('active');}

 exitbtn.onclick= () =>{
 	popup.classList.remove('active');
 	main.classList.remove('active');}

 continuebtn.onclick = () =>{
 	console.log("clicked continue button");
 	quiz_sec.classList.add('active');
 	popup.classList.remove('active');
 	main.classList.remove('active');
 	quizBox.classList.add('active');
    showQuestions(0);
    questionCounter(1);}

 tryAgainbtn.onclick = () =>{

     quizBox.classList.add('active');
     nxtBtn.classList.remove('active');
     resultBox.classList.remove('active');
    
     questionCount=0; 
     questionNumb=1;
     userScore=0;
     showQuestions(questionCount);
     questionCount(questionNumb);
     headerScore();

     } 
gohome.onclick = () =>{

     quiz_sec.classList.remove('active');
     nxtBtn.classList.remove('active');
     resultBox.classList.remove('active');
    
     questionCount=0; 
     questionNumb=1;
     userScore=0;
     showQuestions(questionCount);
     questionCount(questionNumb);
     headerScore();

     } 


 let questionCount=0; 
 let questionNumb=1;
 let userScore=0;
 console.log("questioncount before inceremtn",questionCount);

 

 nxtBtn.onclick = () =>{
                             if(questionCount < questions.length-1){    //question.length-1 = 4
                                    questionCount++; //
                                    showQuestions(questionCount); 
                                    questionNumb++;
                                    questionCounter(questionNumb);
                                    }
                                 else{
                                         showResult();
                                         console.log("result box activated");
                                         
                                   }

                             nxtBtn.classList.remove('active');
                            console.log("active class activated");

                         }


 function showQuestions(index){
 	                           questionText.textContent=`${questions[index].num} . ${questions[index].question}`;
                                 console.log("questioncount after incremetn ",questionCount);
                                 console.log( "index number : ",index);
                                 let optionTag =`<div class="option"><span>${questions[index].options[0]}</span> </div>
                                                 <div class="option"><span>${questions[index].options[1]}</span> </div>
                                                 <div class="option"><span>${questions[index].options[2]}</span> </div>
                                                 <div class="option"><span>${questions[index].options[3]}</span> </div>`;
                                 console.log("optionTage value is here",optionTag);
                                 optionList.innerHTML = optionTag;
                                 nxtBtn.classList.remove('active');
                                 console.log("active class deactivated");

                                 let options=document.querySelectorAll('.option'); // return nodelist isliye used loop for iterate
                                  for(let i=0;i<options.length;i++)
                                  {
                                       
                                       options[i].addEventListener("click",function()
                                        {
                                            selectedAnswer(this); // 
                                        });

                                  }

                                  
                                
                             }
 function selectedAnswer(answer)
 {
    let useranswer=answer.textContent.trim(); // trim is used to remove spaces textContent used to get or set the text inside an HTML ELEMENT.
    console.log("user answer: ",useranswer);
    let correctanswer=questions[questionCount].answer;
    console.log("correct answer",correctanswer);
    let alloptions=optionList.children.length; 

        if(useranswer.toLowerCase()===correctanswer.toLowerCase()) // converting both answers in lower case
        {
            // console.log("yes this is correct");
            answer.classList.add('correct'); // css property of answer.correct  execute
            userScore++;
            console.log("user : ",userScore);
            headerScore();
        }
        else{
                // alert("wrong answer");
                answer.classList.add('incorrect'); 
            }
            
        // if user has selected any one option then other options will be disabled
        for(let i=0;i<alloptions;i++)
        {
            optionList.children[i].classList.add('disabled');
            nxtBtn.classList.add('active');
            console.log("active class activated");
        }
        
 }

 function questionCounter(index){
                                     let totalquestion=document.querySelector('.quesion-total');
                                     totalquestion.innerHTML=`${index} of ${questions.length} questions`;
                                }
         
 function headerScore(){
    let score=document.querySelector('.header-score');
    score.textContent=`score: ${userScore}/${questions.length}`;
 }


 function showResult(){
 quizBox.classList.remove('active');
 resultBox.classList.add('active');
 console.log("resilt box got activeaeted in showResult function");
 const score=userScore;
 const total=questions.length;
 restulScore.textContent=`your score ${score} out of ${total}`;


 /*-------------------------------result box animation and percentage ----------------------------------*/

 let circularProgress=document.querySelector('.circular-progress');
 let progressValue=document.querySelector('.progress-values');
 let progress_start_Value=0;
 let progress_end_Value=(userScore / questions.length)*100;
 console.log(progress_end_Value);
 let speed=50; // 1000ms=1s


 let animation_result=setInterval(()=>{
     if(progress_start_Value === progress_end_Value )
     {
     clearInterval(animation_result);
     }
     else{
     progress_start_Value++;
     progressValue.textContent=`${progress_start_Value}%`;
     circularProgress.style.background=`conic-gradient(#c40094 ${progress_start_Value * 3.6}deg, rgba(255,255,255,.1) ${progress_start_Value * 3.6}deg)`;
      }

     },speed);


}

});

