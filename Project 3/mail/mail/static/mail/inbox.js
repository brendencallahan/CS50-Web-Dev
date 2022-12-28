document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#compose-form').addEventListener('submit', send_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

async function get_emails(mailbox) {

  // Use API to get all emails then parse response
  try {
    const response = await fetch(`/emails/${mailbox}`);
    const data = await response.json();
    return data;

  // Handle errors
  } catch(err) {
    console.log(err);
  }
}


async function send_email(event) {

  event.preventDefault();
// Get values from form
  const email_recipient = document.querySelector('#compose-recipients').value;
  const email_subject = document.querySelector('#compose-subject').value;
  const email_body = document.querySelector('#compose-body').value;

  // post email to database, using api
  try {
    const response = await fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: email_recipient,
        subject: email_subject,
        body: email_body
      })
    })

  // Redirect to inbox, on response
    const data = await response.json();
    load_mailbox('sent');

  } catch(err) {
    console.log(`Error: ${err}`);
  }
}


function compose_email() {

  // show compose view and hide other views
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#mail-view').style.display = 'none';

  // clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function reply_email() {
  //TODO
  //TODO
  //TODO
  //TODO
  //TODO
  //TODO
  return;
}

async function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#mail-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#heading').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;


  // Reset content
  document.querySelector('#emails-wrapper').innerHTML = '';

  // Create list and append list item emails to it
  const email_list = document.createElement('ul');

  const emails = await get_emails(mailbox);
  emails.forEach(element => {

    // Create elements for emails
    const sender = document.createElement('span');
    const subject = document.createElement('span');
    const timestamp = document.createElement('span');
    const email_list_button = document.createElement('button');
    const email_list_item = document.createElement('li');

    // Fill elements with emails
    sender.innerHTML = `${element.sender}:`;
    subject.innerHTML = element.subject;
    timestamp.innerHTML = element.timestamp;

    // Add listener for click, to be able to load specific email
    email_list_button.addEventListener('click', () => load_mail(element.id));

    // Append emails to list
    email_list_button.append(sender, subject, timestamp);
    email_list_item.append(email_list_button);
    email_list.append(email_list_item);

    // Add styling
    sender.classList.add('pr-2');
    timestamp.classList.add('ml-auto');
    email_list.classList.add('list-group');
    email_list_item.classList.add('list-unstyled');
    email_list_button.classList.add('list-group-item', 'w-100', 'd-inline-flex', 'rounded');

    // Conditional styling
    if (!element.read) {
      email_list_button.classList.add('bg-white');
    } else {
      email_list_button.classList.add('bg-secondary');
    }

  });
  // Add list to DOM
  document.querySelector('#emails-wrapper').append(email_list);
}

async function load_mail(email_id) {

  // Show the mailbox and hide other views
  document.querySelector('#mail-view').style.display = 'block';
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  // Set read element to true
  await fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true,
    })
  });

  // Get email
  const email_resp = await fetch(`/emails/${email_id}`);
  const email = await email_resp.json();

  // Create elements
  const page = document.querySelector('#mail-view');
  const sender = document.createElement('p');
  const recipients = document.createElement('p');
  const subject = document.createElement('h3');
  const body = document.createElement('p');
  const timestamp = document.createElement('p');
  const reply_button = document.createElement('button');
  const archive_button = document.createElement('button');

  // Fill elements with text
  sender.innerHTML = email.sender;
  recipients.innerHTML = email.recipients;
  subject.innerHTML = email.subject;
  body.innerHTML = email.body;
  timestamp.innerHTML = email.timestamp;
  reply_button.innerHTML = (`Reply`);
  archive_button.innerHTML = (`${!email.archived ? 'Archive' : 'Unarchive'}`)

  // Add button functionality
  reply_button.addEventListener('click', () => reply_email(email_id))
  archive_button.addEventListener('click', async () => {
    await fetch(`/emails/${email_id}`, {
      method: 'PUT',
      body: JSON.stringify({
        archived: !email.archived,
      })
    });
    await load_mailbox(`${email.archived ? 'archive' : 'inbox'}`);
  });

  // Clear page so it doesn't stack with new emails
  page.innerHTML = ('');
  // Append to DOM
  page.append(sender, recipients, subject, body, timestamp, reply_button, archive_button);
}