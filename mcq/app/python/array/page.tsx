// components/ArrayMCQs.tsx
'use client';

import { useState } from 'react';

type UserAnswers = {
  [key: string]: string; // mapping question keys (q1, q2, ...) to answers (A, B, C, D)
};

export default function ArrayMCQs() {
  const correctAnswers: { [key: string]: string } = {
    q1: 'A',
    q2: 'C',
    q3: 'B',
    q4: 'A',
    q5: 'B',
    q6: 'A',
    q7: 'A',
    q8: 'B',
    q9: 'A',
    q10: 'A',
  };

  const [userAnswers, setUserAnswers] = useState<UserAnswers>({});
  const [score, setScore] = useState<number | null>(null);
  const [feedbackColor, setFeedbackColor] = useState<string>('');

  const handleAnswerChange = (question: string, answer: string) => {
    setUserAnswers({
      ...userAnswers,
      [question]: answer,
    });
  };

  const checkAnswers = () => {
    let newScore = 0;
    for (let question in correctAnswers) {
      if (userAnswers[question] === correctAnswers[question]) {
        newScore++;
      }
    }
    setScore(newScore);

    // Set feedback color based on score
    if (newScore === 10) {
      setFeedbackColor('text-green-500');
    } else if (newScore >= 7) {
      setFeedbackColor('text-orange-500');
    } else {
      setFeedbackColor('text-red-500');
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white shadow-md rounded-lg">
      <h1 className="text-center text-2xl font-bold mb-6">Array MCQs - GATE Level</h1>

      {/* Question 1 */}
      <div className="mb-4">
        <p className="font-semibold">
          1. Consider the following array of integers: `arr = [1, 4, 2, 10, 8, 3]`. What will be the output of the following code segment?
        </p>
        <pre className="bg-gray-100 p-2 text-sm my-2">
          arr.sort(reverse=True)<br />
          print(arr[1:4])
        </pre>
        <div>
          <label className="block">
            <input type="radio" name="q1" value="A" onChange={() => handleAnswerChange('q1', 'A')} />
            A) [10, 8, 4]
          </label>
          <label className="block">
            <input type="radio" name="q1" value="B" onChange={() => handleAnswerChange('q1', 'B')} />
            B) [10, 8, 3]
          </label>
          <label className="block">
            <input type="radio" name="q1" value="C" onChange={() => handleAnswerChange('q1', 'C')} />
            C) [10, 4, 2]
          </label>
          <label className="block">
            <input type="radio" name="q1" value="D" onChange={() => handleAnswerChange('q1', 'D')} />
            D) [8, 4, 2]
          </label>
        </div>
      </div>

      {/* Add more questions here following the same pattern */}

      <button
        onClick={checkAnswers}
        className="w-full py-2 mt-6 bg-blue-500 text-white rounded-md hover:bg-blue-600"
      >
        Submit Answers
      </button>

      {score !== null && (
        <p className={`mt-4 text-xl font-bold ${feedbackColor}`}>
          You got {score} out of 10 correct!
        </p>
      )}
    </div>
  );
}
