from django.shortcuts import render
import torch
from transformers import BertTokenizer, BertForSequenceClassification

def index(request):
    if request.method == 'POST':
        input_text = request.POST['security_requirement']

        # Load the BERT model and tokenizer (same code as in your previous example)
        model_path = 'bert_model'
        tokenizer = BertTokenizer.from_pretrained(model_path)
        model = BertForSequenceClassification.from_pretrained(model_path)
        model.eval()

        # Tokenize and convert the input text to input IDs
        input_ids = tokenizer.encode(input_text, add_special_tokens=True)
        input_ids = torch.tensor(input_ids).unsqueeze(0)

        # Forward pass to get predictions
        with torch.no_grad():
            outputs = model(input_ids)

        logits = outputs.logits
        probs = torch.softmax(logits, dim=1)
        predicted_class = torch.argmax(probs, dim=1).item()

        class_labels = model.config.id2label
        predicted_label = class_labels[predicted_class]

        label_mappings = {
            'LABEL_0': 'Access control',
            'LABEL_1': 'Accountability',
            'LABEL_2': 'Availability',
            'LABEL_3': 'Confidentiality',
            'LABEL_4': 'Functional',
            'LABEL_5': 'Integrity',
            'LABEL_6': 'Operational',
            'LABEL_7': 'Other'
        }
        predicted_label = label_mappings.get(predicted_label, 'Unknown')

        label_descriptions = {
            'Access control': 'Access Control is a fundamental cybersecurity concept that involves the management of permissions and restrictions to control who can access specific resources. It ensures that only authenticated and authorized users have access to system resources, protecting against unauthorized entry or data breaches.',

            'Accountability': 'Accountability is a cybersecurity principle that establishes the ability to trace actions and events uniquely to specific entities or individuals. It plays a crucial role in non-repudiation, deterrence of malicious activities, fault isolation, intrusion detection and prevention, and facilitates post-incident recovery and legal actions.',

            'Availability': 'Availability in cybersecurity refers to the continuous and reliable operation of a system or service over time. It encompasses factors such as system uptime, redundancy, and disaster recovery planning to ensure that systems remain accessible and operational, even in the face of disruptions or attacks.',

            'Confidentiality': 'Confidentiality is a core cybersecurity principle that focuses on the protection of sensitive information from unauthorized access or disclosure. It encompasses encryption, access controls, and data classification to maintain the privacy and security of sensitive data.',

            'Functional': 'Functional cybersecurity considerations involve the assessment of how security mechanisms and features are integrated into a system or process to perform specific functions. It encompasses evaluating the effectiveness of security controls and features in safeguarding a system.',

            'Integrity': 'Integrity, in cybersecurity, revolves around ensuring that data remains accurate and trustworthy throughout its lifecycle. It guards against unauthorized alterations, tampering, or corruption of data, preserving data reliability and trustworthiness.',

            'Operational': 'Operational security, often associated with military and critical infrastructure, involves the identification of critical information and the analysis of actions related to military operations or sensitive activities. It focuses on protecting sensitive operations and information from adversaries.',

            'Other': 'The "Other" category is typically used to classify information or requirements that do not fit into any of the above-defined cybersecurity categories. It serves as a general category for miscellaneous or yet-to-be-categorized items in the cybersecurity context.',
        }


        predicted_label_description = label_descriptions.get(predicted_label, 'Unknown')

        return render(request, 'home/classification_result.html', {'input_text': input_text, 'predicted_label': predicted_label, 'predicted_label_description': predicted_label_description})
    return render(request, 'home/index.html')