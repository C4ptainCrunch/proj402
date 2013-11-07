{% load i18n %}
{% comment %}

# Copyright 2011, hast. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU Affero General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.

{% endcomment %}
{% if msg %}
<p>{{ msg }}</p>

{% else %}

<p><strong>Search: {{ query }}</strong></p>

{% for doc in docs %}
	<div style="margin: 5px;">
		<p><a href="{% url view_file doc.id %}" onclick="return Iload('{% url view_file doc.id %}');">
			<strong>{{ doc.name }}</strong>
		</a><br>
		<i>{% if doc.description %}{{ doc.description }}{% else %}<span style="color: #888">Still no description..</span>{% endif %}</i><br>
		<small>Uploaded by <i>{{ doc.owner.first_name }} {{ doc.owner.last_name }}</i> in 
		       <a href="{% url course_show doc.refer.slug %}"
			  onclick="return Iload('{% url course_show doc.refer.slug %}');">
			{{ doc.refer.name }}</a></small>
	</div>
{% endfor %}

{% endif %}

